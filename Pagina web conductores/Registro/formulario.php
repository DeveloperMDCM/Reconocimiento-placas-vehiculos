
<style type="text/css">
 .imagenindex {
   display: none;
 }
 </style>

<?php 
 include ('src/conexion.php');
 

?>

<h1 class="text-center">NUEVO ADMINISTRADOR</h1>
<form  class="formulario" action="Guardar/guardar.php" method="post" >
  
    <div class="card" style="width: 21rem;">
<div class="card-body ">
       
        <div><span>Correo: <input required    autofocus    placeholder="Correo" class="form-control " type="text" name="Email" ></span></div>
        <div><span>Contraseña: <input required autofocus placeholder="Contraseña" class="form-control" type="password"  name="contraseña"  ></span></div>
        <span>Rol:</span>
        <select  class="custom-select  mb-4 " name="rol"  autofocus  >
           <?php 
           $sql=$miconexion->query("SELECT * FROM `Role` WHERE id_rol = 1");
           while($fila=$sql->fetch_array()){
             echo "<option value='".$fila['Rol']."'>".$fila['Rol']."</option>";
           }           
           ?>
        </select> 
        <button type="submit" name="enviar" class="btn btn-success w-100 ">Registrar</button>
       </div>
       </form>
       <!-- copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria -->