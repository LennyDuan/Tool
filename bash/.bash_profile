### Example of NavBar top
export PS1="\[\033[36m\]\u $ \[\033[m\]\[\033[33;1m\]\w\[\033[m\]: " 
export CLICOLOR=1 
export LSCOLORS=gxfxcxdxbxegedabagacad
export PS2=" --> | "

# basics
alias l='ls'
alias la='ls -a'
alias ll='ls -al'
alias e='exit'
alias m='more'
alias h='history'
alias cd..='cd ..'
alias ..='cd ..'

# Give Failed/Success After a command line
PROMPT_COMMAND=__prompt_command # Func to gen PS1 after CMDs
__prompt_command() {
	local EXIT="$?"             
	local RED='\033[0;31m'
	local GREEN='\033[0;32m'
	if [ $EXIT != 0 ]; then
		echo -e "${RED}Failed"
	else
		echo -e "${GREEN}Success"
	fi
}
