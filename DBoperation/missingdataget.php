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
          $stmt = $conn->prepare("SELECT serial_id,MP_fullname,missing_id,m_date,m_mounth,m_year,M_location,MP_image FROM missing_table WHERE missing_person_id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($serial,$name,$id,$date,$mounth,$year,$subject,$image);
 
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['id'] = $id; 
            $temp['name'] = $name; 
            $temp['photo'] = $image;
            $temp['rank'] ="Location :".' '. $subject; 
            $temp['batch'] ="Date :".' '. $date.'-'.$mounth.'-'.$year; 
            $temp['serial'] = $serial;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);
