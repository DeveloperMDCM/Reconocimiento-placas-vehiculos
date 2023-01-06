
<?php
//   copyring moises-canaria
//   copyring moises-canaria
//   copyring moises-canaria
//   copyring moises-canaria
//   copyring moises-canaria
//   copyring moises-canaria
//   copyring moises-canaria
    include '../src/conexion.php'; 
    $infomacion =[
      $correo = $_POST['Email'],
      $contraseña = $_POST['contraseña'],
      $rol = $_POST['rol']
    ];
    //Guardame los datos de mi formulario de registro que recibo por post
    $query = "INSERT INTO `conductores`.`administrador`(Email, contraseña, R_admin) VALUES('$correo','$contraseña','$rol')";
    $resultado = $miconexion->query($query);
    if ($resultado) {
        //Si se crea un nuevo registro mandame al listado de registro
        header("location: ../index.php?page=admins");
    }
?>



 