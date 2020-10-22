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
          $stmt = $conn->prepare("SELECT subject,notice,date,month,year FROM employee_notice WHERE Id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($subject,$notice,$date,$month,$year);
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['subject'] = $subject; 
            $temp['notice'] = $notice; 
            $temp['date'] = $date;
            $temp['month'] = $month; 
            $temp['year'] = $year;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);