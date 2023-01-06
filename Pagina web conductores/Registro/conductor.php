
<style type="text/css">
 .imagenindex {
   display: none;
 }
 </style>

<?php 
 include ('src/conexion.php');
?>
   
<h1 class="text-center">NUEVO CONDUCTOR</h1>
<form  class="formulario" action="Guardar/g_conductor.php" method="post"  enctype="multipart/form-data" >

    <div class="card" style="width: 21rem;">
    <div class="card-body ">
       
        <div><span>Placa: <input required    autofocus    placeholder="Placa" class="form-control " type="text" name="Placa" ></span></div>
        <div><span>Nombre: <input required    autofocus    placeholder="Nombre" class="form-control " type="text" name="Nombre" ></span></div>
        <div><span>Edad: <input required    autofocus    placeholder="Edad" class="form-control " type="number" name="Edad" ></span></div>
        <div><span>Cedula: <input required    autofocus    placeholder="Cedula" class="form-control " type="number" name="Cedula" ></span></div>
        <div><span>Color: <input required    autofocus    placeholder="Color" class="form-control " type="text" name="Color" ></span></div>
        <div><span>Vehiculo:</span>
        <select  class="custom-select  mb-4 " name="Vehiculo"  autofocus  value="<?php echo $datos['R_admin']; ?>">
        <option value="">Seleccione</option>
           <option value="Carro">Carro</option>
           <option value="Moto">Moto</option>
        </select> </div>
        <div><span>Genero:</span>
         <select  class="custom-select  mb-4 " name="Genero"  autofocus>
           <option value="">Seleccione</option>
           <option value="Masculino">M</option>
           <option value="Femenino">F</option>
         </select> </div>
         <div><span>Ciudad: <input required    autofocus    placeholder="Ciudad" class="form-control " type="text" name="Ciudad" ></span></div>
         <div><span>Rol:</span>
        <select  class="custom-select  mb-4 " name="Rol"  autofocus  value="<?php echo $datos['R_admin']; ?>">
           <?php 
           $sql=$miconexion->query("SELECT * FROM `Role`");
           while($fila=$sql->fetch_array()){
             echo "<option value='".$fila['Rol']."'>".$fila['Rol']."</option>";
           }           
           ?>
        </select> 
        </div>
   
        <div class="input-group mb-3">
  <div class="input-group-prepend">
    <span class="input-group-text" id="inputGroupFileAddon01">Subir</span>
  </div>
  <div class="custom-file">
    <input type="file" name="Imagen" required class="custom-file-input" id="inputGroupFile01" aria-describedby="inputGroupFileAddon01">
    <label class="custom-file-label" for="inputGroupFile01">Imagen</label>
  </div>
</div>

      <button type="submit" name="enviar" class="btn btn-success w-100 ">Registrar</button>
      </div>
      </div>

</form>


copyring moises-canaria
