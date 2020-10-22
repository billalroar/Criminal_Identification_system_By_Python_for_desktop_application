<?php 
 
    class DBOperation{
 
        private $con; 
 
        function __construct(){
 
            define('DB_HOST', 'localhost');
            define('DB_USER', 'root');
            define('DB_PASS', '');
            define('DB_NAME', 'policedb');
 
            $this->con = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
 
            //Checking if any error occured while connecting
            if (mysqli_connect_errno()) {
                echo "Failed to connect to MySQL: " . mysqli_connect_error();
                die();
                }
 
        }
 
        /*CRUD -> C -> CREATE */
 
        public function createUser($phoneNumber, $pass, $date){
            if($this->isUserExist($phoneNumber)){
                return 0; 
            }else{
                $password = md5($pass);
                $stmt = $this->con->prepare("INSERT INTO `registration` (`id`, `phonenumber`, `password`, `date`) VALUES (NULL, ?, ?, ?);");
                $stmt->bind_param("sss",$phoneNumber,$password,$date);
 
                if($stmt->execute()){
                    return 1; 
                }else{
                    return 2; 
                }
            }
        }
 
        public function userLogin($PhoneNumber, $pass){
            $password1 = md5($pass);
            $stmt = $this->con->prepare("SELECT serial_id FROM registeremployee WHERE phone_number = ? AND password = ?");
            $stmt->bind_param("ss",$PhoneNumber,$password1);
            $stmt->execute();
            $stmt->store_result(); 
            return $stmt->num_rows > 0; 
        }
 
        public function isUsereligible($PhoneNumber){
            if ($this->isUserExist($PhoneNumber))
            {
                return 2;
            }
            else
            {
                 $stmt = $this->con->prepare("SELECT serial_id FROM employtable WHERE Phonenumber = ?");
                 $stmt->bind_param("s",$PhoneNumber);
                 $stmt->execute();
                 $stmt->store_result(); 
                 if ($stmt->num_rows > 0) {
                     return 0;
                 }
                 else
                 {
                    return 1;
                 }
            }
        }
         
 
        private function isUserExist($phoneNumber){
            $stmt = $this->con->prepare("SELECT serial_id FROM registeremployee WHERE phone_number = ?");
            $stmt->bind_param("s", $phoneNumber);
            $stmt->execute(); 
            $stmt->store_result(); 
            return $stmt->num_rows > 0; 
        }
 
    }

