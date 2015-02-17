#!/bin/bash



cat to.csv | while read line
	 do
		set -- "$line"
		IFS=";"; declare -a Array=($*)
#DEBUG		echo "${Array[@]}"
#DEBUG
		echo "./bin/send.py \"${Array[0]}\" \"${Array[1]}\" \"${Array[2]}\""
#Send		./bin/send.py \"${Array[0]}\" \"${Array[0]}\" \"${Array[0]}\"

	done
