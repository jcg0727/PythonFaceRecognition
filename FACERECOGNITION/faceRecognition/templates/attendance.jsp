<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script>
  src="https://code.jquery.com/jquery-3.6.0.slim.js"
  integrity="sha256-HwWONEZrpuoh951cQD1ov2HUK5zA5DwJ1DNUXaM6FsY="
  crossorigin="anonymous"></script>
</head>

<body>
 <form action="http://localhost/hs/attendance/attendanceCheck" id="test" method="post">
      <input type="hidden" name="checkId" id="checkId" value="{{a}}">
      <input type="hidden" name="student_no" id="student_no" value="{{b}}">
      <input type="hidden" name="class_no" id="class_no" value="{{c}}">
 </form>

<script type="text/javascript">

   if("{{a}}" == "{{b}}"){
      alert("출석 성공");
      
      var form = document.getElementById("test");
      // 컨트롤러에 checkId(파이선이 내뱉는 값) 과 studentNo(학번으로 넣은 값) 전송
      form.submit();
//       history.go(-1);
      

   } else{
      alert("인증 실패");
      
      
      history.go(-1);
      
   }
   
</script>
</body>
</html>









