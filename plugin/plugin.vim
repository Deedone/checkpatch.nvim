

function! CheckpatchGetScriptPath()
	return get(g:, "checkpatch_path", '')
endfunction

function! CheckpatchIsEnabled()
	return get(g:, "checkpatch_enabled", 0)
endfunction
