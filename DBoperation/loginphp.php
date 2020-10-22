<?php 
 
 require_once dirname(__FILE__).'/DBOperation.php';
 
 $product = array(); 
 
if($_SERVER['REQUEST_METHOD']=='POST'){
    if(isset($_POST['phoneNumber']) and isset($_POST['password'])){
        $db = new DBOperation(); 
 
        if($db->userLogin($_POST['phoneNumber'], $_POST['password'])){
            
 
            //connecting to database and getting the connection object
            $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
            //Checking if any error occured while connecting
            if (mysqli_connect_errno()) {
                echo "Failed to connect to MySQL: " . mysqli_connect_error();
                die();
            }
            $stmt = $conn->prepare("SELECT Firstname,Middlename,Lastname,Batchid,Rank,Imagepath FROM employtable WHERE Phonenumber = ?");
 
            //executing the query 
            $stmt->bind_param("s",$_POST['phoneNumber']);
            $stmt->execute();
 
            //binding results to the query 
            $stmt->bind_result($Firstname,$Middlename,$Lastname,$Batchid,$rank,$Imagepath);
 
            //traversing through all the result 
            while($stmt->fetch()){
                $product['error'] = false; 
                $product['id'] = $Batchid; 
                $product['rank'] = $rank;
                $product['name'] = $Firstname.' '.$Middlename.' '.$Lastname; 
                $product['image'] = $Imagepath;
            }
 
            
        }else{
            $product['error'] = true; 
	    $password1= md5($_POST['password']);
	    $product['pass'] = $password1;
            $product['message'] = "Invalid username or password";          
        }
 
    }else{
        $product['error'] = true; 
        $product['message'] = "Required fields are missing";
    }
}
else{
    $product['error'] = true; 
    $product['message'] = "Invalid Request";
}
 
echo json_encode($product);