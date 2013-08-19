<head><title>Multiply</title>
%# This will add a style sheet to our web page.  The /public
%# directory will be served through bottle.
<link type="text/css" rel="stylesheet" href="public/styles.css">
</head>
<body>
	<h1>{{greeting}}</h1>

% for char in str(greeting):
{{char * 2}}
% end

</body>