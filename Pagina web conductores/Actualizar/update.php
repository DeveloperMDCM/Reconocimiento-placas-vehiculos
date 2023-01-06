
<?php 
include '../src/conexion.php'; 

//  copyring moises-canaria
// copyring moises-canaria
// copyring moises-canaria

// copyring moises-canaria 
$id=$_REQUEST['id'];
  $email = $_POST['Email'];
  $contraseña = $_POST['contraseña'];
  $rol = $_POST['rol'];
  //Actualizame mi mi tabla en la base de datos y asignale mis variables por post
$query = "UPDATE `conductores`.`administrador` SET Email = '$email' , contraseña= '$contraseña', R_admin = '$rol' WHERE `administrador`.`id_administrador` = '$id'";
$resultado = $miconexion->query($query);
//redirigime al listado de usuarios
header("location: ../index.php?page=admins");
?>
