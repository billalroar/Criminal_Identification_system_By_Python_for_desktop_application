<?php 
 
 
 //database constants
 define('DB_HOST', 'localhost');
 define('DB_USER', 'root');
 define('DB_PASS', '');
 define('DB_NAME', 'policedb');
 
 //connecting to database and getting the connection object
 $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
 
 //Checking if any error occured while connecting
 if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
    die();
 }

 if($_SERVER['REQUEST_METHOD']=='POST'){
    if(isset($_POST['id']) and isset($_POST['value'])){
          //creating a query
          $stmt = $conn->prepare("SELECT serial_id,criminal_fname, criminal_mname, criminal_lname,criminal_id,criminal_involvedcaseid,criminal_involvedcasesubject,criminal_firstimage ,criminal_secoundimage,criminal_thirdimage FROM criminal_record WHERE criminal_id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($serial,$namef, $namem, $namel,$id,$caseid,$subject,$image1,$image2,$image3);
 
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['id'] = $id; 
            $temp['name'] = $namef.' '.$namem.' '.$namel; 
            if($image1 != "appsFileImage/icon_persion128.png"){
              $temp['photo'] = $image1;
            }
            if($image2 != "appsFileImage/icon_persion128.png"){
              $temp['photo'] = $image2;
            }
            if($image3 != "appsFileImage/icon_persion128.png"){
              $temp['photo'] = $image3;
            }
            $temp['rank'] = $subject; 
            $temp['batch'] = "Case ID :".' '.$caseid;
            $temp['serial'] = $serial;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);
