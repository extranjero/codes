#Heredoc string syntax
print <<"EOF";
	This is the first way of creating
    here document ie. multiple line string.
EOF

#Heredoc execute syntax
print <<`EOC`
	echo hi there
	echo lo there
EOC

#Heredoc stack
#
print <<"foo", <<"bar"
	I said foo
foo
	I said bar
bar
