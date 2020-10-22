<?php 
 
 
 //database constants
 define('DB_HOST', 'localhost');
 define('DB_USER', 'root');
 define('DB_PASS', '');
 define('DB_NAME', 'policedb');
 
 //connecting to database and getting the connection object
 $con = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
 
 //Checking if any error occured while connecting
 if (mysqli_connect_errno()) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
    die();
 }

 if($_SERVER['REQUEST_METHOD']=='POST'){
    if(isset( $_POST['phoneNumber'],$_POST['password'],$_POST['date']))
    {
          $products = array(); 
          $password = md5($_POST['password']);
          $stmt = $con->prepare("INSERT INTO `registeremployee` (`phone_number`, `password`, `date`) VALUES (?, ?, ?);");
          $stmt->bind_param("sss",$_POST['phoneNumber'],$password,$_POST['date']);
 
          if($stmt->execute()){
            $products['error'] = false; 
            $products['message'] = "User registered successfully"; 
          }
          else{
            $products['error'] = true; 
            $products['message'] = "Some error occurred please try again"; 
          }
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);