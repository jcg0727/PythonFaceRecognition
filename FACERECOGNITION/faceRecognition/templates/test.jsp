<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script
  src="https://code.jquery.com/jquery-3.6.0.slim.js"
  integrity="sha256-HwWONEZrpuoh951cQD1ov2HUK5zA5DwJ1DNUXaM6FsY="
  crossorigin="anonymous"></script>
</head>
<body>
 <form action="http://localhost/hs/common/login.do" id="loginForm" method="post">
      <input type="hidden" name="id" id="id" value="{{b}}">
      <input type="hidden" name="pwd" id="pwd" value="{{c}}">
<!--       <button type="submit" id="submit"></button> -->
 </form>

<script type="text/javascript">
	if("{{a}}" == "{{b}}"){
		alert("인증되었습니다")
		var form = document.getElementById("loginForm");
		form.submit();
	}else{
		alert("아닌데여");
		history.go(-1);
	}

</script>
</body>
</html>










