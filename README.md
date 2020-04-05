# checkpatch.nvim
>Simple Kernelstyle linter

This plugin is a front-end for `checkpatch.pl` script. It automaticlly runs the script every time you save your .c or .h files and shows errors in the editor.

- [Install](#install)
- [Configuration](#configuration)
- [Screenshots](#screensots)



##  Install

### Requierments
- Latest version of [neovim](https://neovim.io/)
- Perl
- checkpatch script from kernel source tree

For vim-plug
```viml
Plug 'Deedone/checkpatch.nvim', { 'do': ':UpdateRemotePlugins' }

let g:checkpatch_enabled = 1
let g:checkpatch_path = "/path/to/checkpatch.pl"
```
For dein.vim

```viml
call dein#add('Deedone/checkpatch.nvim')
let g:checkpatch_enabled = 1
let g:checkpatch_path = "/path/to/checkpatch.pl"
```

If something breaks try to execute `:UpdateRemotePlugins`

## Configuration
### Variables
```viml
let g:checkpatch_path = "/path/to/checkpatch.pl"
let g:checkpatch_enabled = 1
```
### Commands
```viml
:CheckpatchEnable
:CheckpatchDisable
```

## Screenshots


