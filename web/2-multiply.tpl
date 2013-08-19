%# This is a really simple HTML template, but it'll let us 
%# make our web application prettier.
<head><title>Multiply</title></head>
<body>
%# This is how we print variables into our template.  We can
%# also do simple things inside of {{}}, like {{greeting.upper()}}

	<h1>{{greeting}}</h1>

%# We can also run blocks of python code, though we have to
%# end them with %end, since they don't use indents.
% for char in str(greeting):
%# This will echo each character in our greeting twice.
{{char * 2}}
% end

</body>