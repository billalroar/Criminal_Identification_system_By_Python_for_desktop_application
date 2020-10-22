<?php 
 
 $products = array(); 
 
if($_SERVER['REQUEST_METHOD']=='POST'){
    if(isset($_POST['phoneNumber'])){
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
            $stmt = $con->prepare("SELECT serial_id FROM registeremployee WHERE phone_number = ?");
 
            //executing the query 
            $stmt->bind_param("s",$_POST['phoneNumber']);
            $stmt->execute();
            $stmt->store_result(); 
            if($stmt->num_rows > 0)
            {
                $products['error'] = false; 
                $products['message'] = "Done";
            }
	    else
            {
		$products['error'] = false; 
                $products['message'] = "Number not registered";
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