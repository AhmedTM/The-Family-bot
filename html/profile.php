<?php
$host = "192.168.1.5";
$port = 2010;
//echo 'hello from server';
$socket=socket_create(AF_INET, SOCK_STREAM,0) or die("could not create sockret");
//echo 'connected';
socket_connect($socket, $host, $port);
//$cmd="S";
//$json_out = json_encode($cmd);
//socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
//socket_connect($socket, $host, $port);
//sleep(2);
//$cmd="S";
//$json_out = json_encode($cmd);
//socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
//$cmd="S";
//$json_out = json_encode($cmd);
//socket_write($socket, $jsonout, strlen ($json_out)) or die("Could not write outpu\n");
?>
<!DOCTYPE html>
<html>
<title>Family Bot</title>
<head>
	<link rel="stylesheet" type="text/css" href="css/example.css">
	<style>
                #video { border: 1px solid #ccc; border-radius: 20px;  display: block; margin: auto; }
                #canvas { margin-top: 20px; border: 1px solid #ccc; display: block; }
		
        </style>
<!--	<script>
	function forward()
	{
	var ws = new WebSocket("ws://192.168.1.10:2010");
	ws.onopen = function() {ws.send("F"); };
	}

	</script> -->

</head>

<body>
<!--
                Ideally these elements aren't created until it's confirmed that the
                client supports video/camera, but for the sake of illustrating the
                elements involved, they are created with markup (not JavaScript)
        -->
	<div>
	<img id="video" src= "http://192.168.1.5:8081/?action=stream" width="640" height="480"/>
       <!--  <video id="video" width="640" height="480" autoplay></video>
        <canvas id="canvas" width="640" height="480"></canvas> -->
	</div>
	<div>
	<?php
	    //echo 'iam in the script';
            $msg = '';
            
            if (isset($_POST['forward'])) {
		//echo 'iam in the if';
               // ob_start();
               // session_start();
                //$_SESSION['valid'] = true;
                //$_SESSION['timeout'] = time();
                //$_SESSION['username'] = 'Ahmed';
		//$host = "192.168.1.12";
		//$port = 2010;
		//echo 'hello from server';
		//$socket=socket_create(AF_INET, SOCK_STREAM,0) or die("could not create sockret");
		socket_connect($socket, $host, $port);
		$cmd="B";
		//$json_out = json_encode($cmd);
		socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
		//echo 'You have entered valid use name and password';
               // header('Location: /profile.php');
               }
		elseif(isset($_POST['stop'])){
		//ob_start();
                //session_start();
                //$_SESSION['valid'] = true;
                //$_SESSION['timeout'] = time();
                //$_SESSION['username'] = 'Ahmed';
		//$host = "192.168.1.12";
		//$port = 2010;
		//echo 'hello from server';
		//$socket=socket_create(AF_INET, SOCK_STREAM,0) or die("could not create sockret");
		socket_connect($socket, $host, $port);
		$cmd="S";
		//$json_out = json_encode($cmd);
		socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
		}
		elseif(isset($_POST['left'])){
		//echo 'from left';
		//ob_start();
                //session_start();
                //$_SESSION['valid'] = true;
                //$_SESSION['timeout'] = time();
                //$_SESSION['username'] = 'Ahmed';
		$host = "192.168.1.5";
		$port = 2010;
		//echo 'hello from server';
		//$socket=socket_create(AF_INET, SOCK_STREAM,0) or die("could not create sockret");
		socket_connect($socket, $host, $port);
		$cmd="R";
		//$json_out = json_encode($cmd);
		socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
		}
		elseif(isset($_POST['right'])){
		//ob_start();
                //session_start();
                //$_SESSION['valid'] = true;
                //$_SESSION['timeout'] = time();
                //$_SESSION['username'] = 'Ahmed';
		//$host = "192.168.1.12";
		//$port = 2010;
		//echo 'hello from server';
		//$socket=socket_create(AF_INET, SOCK_STREAM,0) or die("could not create sockret");
		socket_connect($socket, $host, $port);
		$cmd="L";
		//$json_out = json_encode($cmd);
		socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
		}
		elseif(isset($_POST['backward'])){
		//ob_start();
                //session_start();
                //$_SESSION['valid'] = true;
                //$_SESSION['timeout'] = time();
                //$_SESSION['username'] = 'Ahmed';
		//$host = "192.168.1.12";
		//$port = 2010;
		//echo 'hello from server';
		//$socket=socket_create(AF_INET, SOCK_STREAM,0) or die("could not create sockret");
		socket_connect($socket, $host, $port);
		$cmd="F";
		//$json_out = json_encode($cmd);
		socket_write($socket, $cmd, strlen ($cmd)) or die("Could not write outpu\n");
		}
		else {
                  $msg = 'Wrong username or password';
               }
         ?>
	</div>
	<form action = "<?php echo htmlspecialchars($_SERVER['PHP_SELF']);  ?>" role="form" method="post">
	<div class="forwardButton">
	<button id="forw" name="forward" class="forwardimg" type="submit">FORWARD</button>
	</div>
	<div class="container">
		<div class="container leftButton">
		<button type="submit" id="left" name="left" class="leftimg">LEFT</button>
		</div>
		<div class="container rightButton">
		<button type="submit" id="right"  name="right" class="rightimg">RIGHT</button>
		</div>
	</div>
	<div class="backwardButton">
	<button type="submit" id="back" class="backwardimg" name="backward">BACK</button>
	</div>
	<div class="container stopButton">
	<button type="submit" id="stop" name="stop" class="centerimg">STOP</button>
	</div>
	</form>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
	<!-- <script type="text/javascript">
	document.getElementById('forw').onclick = function(){
	var ws = new WebSocket("ws://192.168.1.10:2010");
	ws.onopen = function() {ws.send("F"); };
	};
	document.getElementById('back').onclick = function(){
	var ws = new WebSocket("ws://192.168.1.10:2010");
	ws.onopen = function() {ws.send("B"); };
	};
	document.getElementById('left').onclick = function(){
	var ws = new WebSocket("ws://192.168.1.10:2010");
	ws.onopen = function() {ws.send("L"); };
	};
	document.getElementById('right').onclick = function(){
	var ws = new WebSocket("ws://192.168.1.10:2010");
	ws.onopen = function() {ws.send("R"); };
	};
	document.getElementById('stop').onclick = function(){
	var ws = new WebSocket("ws://192.168.1.10:2010");
	ws.onopen = function() {ws.send("S"); };
	};
	</script> -->
</body>
</html>
