<?php 
 
require_once dirname(__FILE__).'/DBOperation.php';
 
$response = array(); 
 
if($_SERVER['REQUEST_METHOD']=='POST'){
    if(isset($_POST['phoneNumber']))
    {
        //operate the data further 
 
        $db = new DBOperation(); 
 
        $result = $db->isUsereligible($_POST['phoneNumber']);
        if($result == 1){
            $response['error'] = true; 
            $response['message'] = "You are not eligible";
        }
        elseif($result == 2){
            $response['error'] = true; 
            $response['message'] = "You are already registered";          
        }
        elseif($result == 0){
          $response['error'] = false; 
          $response['message'] = "Done";          
        }
 
    }
    else{
        $response['error'] = true; 
        $response['message'] = "Required fields are missing";
    }


}else{
    $response['error'] = true; 
    $response['message'] = "Invalid Request";
}
 
echo json_encode($response);