<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Selenium - {{ title }}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <link href="/static/favicon.ico" rel="shortcut icon" type="limited/image/x-icon"/>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <!--<link href="/static/css/bootstrap-responsive.min.css" rel="stylesheet">-->
    <style type="text/css">
        .hero-unit h1 {
            font-size: 50px;
        }

        .hero-unit {
            padding: 50px 60px 10px;
            margin-bottom: 20px;
            background-color: #EEE;
            -webkit-border-radius: 3px;
            -moz-border-radius: 3px;
            border-radius: 3px;
        }

        .label-light {
            opacity: 0.7;
        }
    </style>
</head>

<body>

<div class="navbar navbar-fixed-top">
    <div class="navbar-inner">
        <div class="container">
            <a class="brand" href="#">Selenium test samples</a>

            <div class="nav-collapse collapse">
                <ul class="nav">
                    <li><a href="/lab1/">Lab 1</a></li>
                    <li><a href="/lab2/">Lab 2</a></li>
                    <li><a href="/lab3/">Lab 3</a></li>
                    <li><a href="/about/">About</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="container">

    <div class="hero-unit">
        <h1>{{ get('title', 'No title defined') }}</h1>

        <p>This is a simple marketing. Use it as a starting point to create something more unique.</p>
    </div>

    <div class="row-fluid">
        %body()
    </div>

    <hr>

    <footer>
        <p>&copy; <a href="mailto:black7white@ya.ru">B7W</a> 2012</p>
    </footer>

</div>

<script type="text/javascript" src="/static/js/jquery.min.js"></script>
<script type="text/javascript">
    jQuery('.nav a[href="' + window.location.pathname + '"]').parent().addClass('active');
</script>

% if defined('script'):
%script()
% end

</body>
</html>
