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
          $stmt = $conn->prepare("SELECT persone_name,father_name,curret_address,permanent_address,birth_data,birth_month,bieth_year,gender,religion,marrid,phone_no,email_id,nid_no,passport_no,emergency_name,emergency_relation,emergency_phone,emergency_address,persone_photo FROM servey_info WHERE serial_id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($name,$father_name,$current_address,$permanent_address,$birth_date,$birth_mounth,$birth_year,$gender,$religion,$merried,$phonenumber,$email_id,$nid_no,$passport_no,$e_name,$e_relation,$e_phone,$e_address,$image);
 
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['name'] = $name; 
            $temp['father_name'] = $father_name; 
            $temp['current_address'] = $current_address;
            $temp['permanent_address'] = $permanent_address; 
            $temp['birth'] = $birth_date.'-'.$birth_mounth.'-'.$birth_year;
            $temp['gender'] = $gender;
            $temp['religion'] = $religion;
            $temp['merried'] = $merried;
            $temp['phonenumber'] = $phonenumber;
            $temp['email_id'] = $email_id;
            $temp['nid_no'] = $nid_no;
            $temp['passport_no'] = $passport_no;
            $temp['e_name'] = $e_name;
            $temp['e_relation'] = $e_relation;
            $temp['e_phone'] = $e_phone;
            $temp['e_address'] = $e_address;
            $temp['image'] = $image;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);