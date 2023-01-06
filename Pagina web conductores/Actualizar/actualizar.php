<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Actualizar</title>
  <link rel="stylesheet" href="../css/estilos.css">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
<body>

  <!-- copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria -->

  <style type="text/css">
    .imagenindex {
      display: none;
    }

    <?php


    $id = $_REQUEST['id'];
    include('../src/conexion.php');
    //Muestra los datos que coinciden con el id que quiero actualizar
    $query = "SELECT * FROM administrador WHERE id_administrador='$id'";
    $resultado = $miconexion->query($query);
    // fila de resultado como un array asociativo
    $datos = $resultado->fetch_assoc();
    ?>
  </style>
  <br>
  <br>
  <br> 
  <h1 class="text-center">ACTUALIZAR ADMINISTRADOR</h1>
  <form class="formulario" action="../Actualizar/update.php?id=<?php echo $datos['id_administrador'] ?>" method="POST">

    <div class="card" style="width: 21rem;">
      <div class="card-body ">

        <div><span>Correo: <input  required autofocus placeholder="Tu nombre" class="form-control" type="text" name="Email" value="<?php echo $datos['Email']; ?>"></span></div>
        <div><span>Contraseña: <input required autofocus placeholder="Tu edad" name="contraseña" class="form-control" type="password" value="<?php echo $datos['contraseña']; ?>"></span></div>
        <span>Rol: </span>
        <select class="custom-select  mb-4 " name="rol" autofocus value="<?php echo $datos['R_admin']; ?>">
          <?php
          $sql = $miconexion->query("SELECT * FROM `Role` WHERE id_rol = 1");
          while ($fila = $sql->fetch_array()) {
            echo "<option value='" . $fila['Rol'] . "'>" . $fila['Rol'] . "</option>";
          }
          ?>
        </select>
        <br>
        <button type="submit" name="enviar" class="btn btn-info w-100 ">Actualizar</button>
        <br>
        <br>
        <button type="link" name="enviar" href="../index.php?page=admins" class="btn btn-danger w-100 ">Regresar</button>
      </div>

  </form>
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>

</html>

<!-- copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring pedro-barios
copyring pedro-barios
copyring pedro-barios

copyring moises-canaria -->