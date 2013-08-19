<head><title>Multiply</title>
<link type="text/css" rel="stylesheet" href="public/styles.css">
</head>
<body>
	<h1>Multiply</h1>

	<h2>{{greeting}}</h2>

%# Let's get a little fancier with out embedded python code.
%# Now we'll check and see if we can turn greeting into an integer.
% try:
%    int(greeting)

%# If we can, we'll square it for the user.  If not, we won't.
<h2>{{greeting}} squared is {{int(greeting) * int(greeting)}}</h2>
% except ValueError:
%    pass
% end

%# Now we'll add a simple HTML form that will submit 'a' and 'b' to the
%# script.
	<form method="POST">
		<input type="text" name="a"> X <input type="text" name="b"></br> 
	<input type="submit">
	</form>
</body>