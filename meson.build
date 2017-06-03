project('bench', 'c')

c = run_command('grabber.sh')
sources = c.stdout().strip().split('\n')

static_library('bench', sources)
