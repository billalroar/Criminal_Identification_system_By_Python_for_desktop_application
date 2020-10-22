<?php 
 
 /*
 * Created by Belal Khan
 * website: www.simplifiedcoding.net 
 * Retrieve Data From MySQL Database in Android
 */
 
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
    if(isset($_POST['id'])){
          //creating a query
          $stmt = $conn->prepare("SELECT criminal_fname,criminal_mname,criminal_lname,criminal_age,criminal_gender,criminal_recover,criminal__needrecover,criminal_arrest,criminal_involvedcaseid,criminal_involvedcasesubject,criminal_details,criminal_firstimage,criminal_secoundimage,criminal_thirdimage FROM criminal_record WHERE serial_id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($name1,$name2,$name3,$age,$gender,$recover,$need_recover,$arrest,$case_id,$case_subject,$case_details,$image1,$image2,$image3);
 
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['name'] = $name1.' '.$name2.' '.$name3; 
            $temp['age'] = $age; 
            $temp['gender'] = $gender;
            $temp['recover'] = $recover; 
            $temp['need_recover'] =$need_recover; 
            $temp['arrest'] = $arrest;
            $temp['case_id'] = $case_id;
            $temp['case_subject'] = $case_subject;
            $temp['case_details'] = $case_details;
            $temp['image1'] = $image1;
            $temp['image2'] = $image2;
            $temp['image3'] = $image3;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);