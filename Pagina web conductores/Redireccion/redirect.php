<!-- copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring pedro-barios
copyring pedro-barios
copyring pedro-barios

copyring moises-canaria -->
<?php

    session_start();
    //guardame los datos en variables  post
    $adminUser = [
    $usuario=$_POST['Email'],
    $contraseña=$_POST['contraseña']
    ];
    //CONSULTAR USUARIO Y CONTRASENA EN LA BD
    $conexion=mysqli_connect("localhost", "root", "", "conductores") or die ("Error al conectar la base de datos");
    //Verificame si la contraseña y usuario coinciden 
    $consultarUser= "SELECT * FROM administrador WHERE Email= '$usuario' and contraseña= '$contraseña' and R_admin= 'administrador'";
    $resulUser=mysqli_query($conexion, $consultarUser);
    //dime si exite en la base de datos el usuario y contraseña
      $filas=mysqli_num_rows($resulUser);

      //Si existe mi usuario inicia sesion
      if($filas>0){
        $_SESSION["auth"] = $usuario;
        //$_SESSION["auth"] = VARIABLE CON NOMBRE DE USUARIO Y/O EN BD   $RESULT->USERNAME GMAIL;
        header("Location: ../index.php?page=list"); 
      }else{
        header("Location: ../index.php?page=login"); 
      }
      
      
    
?>




