import pynvim
import subprocess


@pynvim.plugin
class Main(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.enabled = False


    def printHint(self, text, line, type):
        nsid = self.nvim.call("nvim_create_namespace","checkpatch")

        self.nvim.call('nvim_buf_set_virtual_text',self.nvim.current.buffer,nsid,
                int(line) - 1, ((text,type),), [])

    def clearHint(self):
        nsid = self.nvim.call("nvim_create_namespace","checkpatch")
        self.nvim.call('nvim_buf_clear_namespace',self.nvim.current.buffer,nsid,
                0, -1)


    @pynvim.command('CheckpatchEnable', nargs='0')
    def enable(self, args):
        self.enabled = True


    @pynvim.command('CheckpatchDisable', nargs='0')
    def disable(self, args):
        self.enabled = False
        self.clearHint()


    def getReport(self):
        filename = self.nvim.call("expand","%:p")

        path = self.getScriptPath()
        if not path:
            self.nvim.err_write("Cannot locate checkpatch script, please fill g:CheckpatchPath\n")
            return []
        pc = subprocess.Popen([path,"--no-tree","--terse","--no-summary",
            "-f",filename], stdout=subprocess.PIPE)
        pc.wait();
        txt = pc.stdout.read()
        return str(txt).split('\\n');

    def getScriptPath(self):
        path = self.nvim.call("CheckpatchGetScriptPath")
        return path

    @pynvim.autocmd("BufWritePost", pattern="*.c,*.h")
    def run(self):
        if not self.nvim.call("CheckpatchIsEnabled"):
            return
        rep = self.getReport()
        self.clearHint()
        for line in rep:
            data = line.split(':')
            if len(data) < 3:
                continue
            line = data[1]
            msg = ':'.join(data[3:])
            self.printHint(msg, line, 'ErrorMsg')
