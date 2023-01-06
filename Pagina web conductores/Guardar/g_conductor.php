
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
      $Placa = $_POST['Placa'],
      $Nombre = $_POST['Nombre'],
      $Edad = $_POST['Edad'],
      $Cedula = $_POST['Cedula'],
      $Color = $_POST['Color'],
      $Vehiculo = $_POST['Vehiculo'],
      $Genero = $_POST['Genero'],
      $Ciudad = $_POST['Ciudad'],
      $Rol = $_POST['Rol'],
    ];
    $Imagen = addslashes(file_get_contents($_FILES['Imagen']['tmp_name']));  
    //Guardame los datos de mi formulario de registro que recibo por post
    $query = "INSERT INTO `personas` (`placa`, `nombre`, `edad`, `cedula`, `color`, `tipo_vehiculo`, `genero`, `ciudad`, `tipo_persona`,`imagen` )
     VALUES('$Placa','$Nombre','$Edad','$Cedula','$Color','$Vehiculo','$Genero','$Ciudad','$Rol','$Imagen')";
    $resultado = $miconexion->query($query);
    if ($resultado) {
        //Si se crea un nuevo registro mandame al listado de registro
        header("location: ../index.php?page=conductores");
    }
?>



 