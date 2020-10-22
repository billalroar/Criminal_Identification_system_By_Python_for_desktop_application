<?php 
 
 $products = array(); 
 
if($_SERVER['REQUEST_METHOD']=='POST'){
    if(isset($_POST['phoneNumber']) and isset($_POST['password'])){
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
            $stmt = $con->prepare("UPDATE `registeremployee` SET `password`=? WHERE `phone_number`=?;");
 
            //executing the query 
            $password = md5($_POST['password']);
            $stmt->bind_param("ss",$password,$_POST['phoneNumber']);
            if($stmt->execute())
            {
                $products['error'] = false; 
                $products['message'] = "User password changed"; 
            }
            else
            {
                $products['error'] = true; 
                $products['message'] = "Some error occurred please try again"; 
            }
 
    }else{
        $products['error'] = true; 
        $products['message'] = "Required fields are missing";
    }
}
else{
    $products['error'] = true; 
    $products['message'] = "Invalid Request";
}
 
echo json_encode($products);