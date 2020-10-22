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
          $stmt = $conn->prepare("SELECT Firstname,Middlename,Lastname,Rank,Batchno,Batchid,Phonenumber,Emailid,Birthdate,Birthmounth,Birthyear,Gender,Current_address,permanent_address,Unite,fair,fair_date,suspend,suspend_date,Imagepath FROM employtable WHERE serial_id = ?");
 
          //executing the query 
          $stmt->bind_param("s",$_POST['id']);
          $stmt->execute();
 
          //binding results to the query 
          $stmt->bind_result($name1,$name2,$name3,$rank,$batchno,$batchid,$phonenumber,$email,$birth_date,$birth_mounth,$birth_year,$gender,$current_address,$permanent_address,$unite,$fair,$fair_date,$suspend,$suspend_date,$image);
 
          $products = array(); 
 
          //traversing through all the result 
          while($stmt->fetch()){
            $temp = array();
            $temp['name'] = $name1.' '.$name2.' '.$name3; 
            $temp['rank'] = $rank; 
            $temp['batch_id'] = $batchid;
            $temp['batchno'] = $batchno; 
            $temp['phonenumber'] = $phonenumber;
            $temp['email'] = $email;
            $temp['birth'] = $birth_date.'-'.$birth_mounth.'-'.$birth_year;
            $temp['gender'] = $gender;
            $temp['current_address'] = $current_address;
            $temp['permanent_address'] = $permanent_address;
            $temp['unite'] = $unite;
            $temp['fair'] = $fair;
            $temp['fair_date'] = $fair_date;
            $temp['suspend'] = $suspend;
            $temp['suspend_date'] = $suspend_date;
            $temp['image'] = $image;
            array_push($products, $temp);
          }
          
    }
  } 
 //displaying the result in json format 
 echo json_encode($products);