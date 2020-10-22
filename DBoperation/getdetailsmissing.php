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
          $stmt = $conn->prepare("SELECT MP_fullname,MP_address,MP_gender,MP_father,MP_age,m_date,m_mounth,m_year,M_location,M_detail,Mp_image FROM missing_table WHERE serial_id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($name,$address,$gender,$father_name,$age,$missing_date,$missing_mounth,$missing_year,$missing_area,$details,$image);
 
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['name'] = $name; 
            $temp['address'] = $address; 
            $temp['gender'] = $gender;
            $temp['father_name'] = $father_name; 
            $temp['age'] = $age;
            $temp['missing_date'] = $missing_date.'-'.$missing_mounth.'-'.$missing_year;
            $temp['missing_area'] = $missing_area;
            $temp['details'] = $details;
            $temp['image'] = $image;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);