<?php 
include ("../src/conexion.php"); 
 $id=$_REQUEST['id'];
//Eliminame los datos que coincidan con el id
$query = "DELETE FROM administrador WHERE id_administrador='$id';";
$resultado = $miconexion->query($query);
//llevame a la lista de usuarios 
header("location: ../index.php?page=admins");
?>
<!-- copyring moises-canaria
copyring moises-canaria
copyring moises-canaria


copyring moises-canaria -->