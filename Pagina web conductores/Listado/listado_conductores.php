
<!-- copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria -->
<style>
  .card:hover{
    box-shadow: 2px 2px 2px #999;
  }
    .card {
        margin: 7px;
        max-width: 300px;
       
        display: inline-block;
        border-radius: 30px;
    }
    img{
      border-radius: 30px 30px 0 0;
    }
</style>

<table class="table  table-bordered table-dark table-hover "   >

  
    <b><h1 class="text-center">LISTADO DE CONDUCTORES</h1> </b>
     <form class="form-inline my-2 my-lg-0" method="post" action="index.php?page=conductores">
     <center> <input class="form-control mr-sm-2" type="search" placeholder="Busqueda" aria-label="Search" name="query" id="query" style="text-align:center">
        <button class="btn btn-success w-100" type="submit">Buscar</button>
    </form>
      <?php
        require ('src/conexion.php');
        
          if(isset($_POST['query'])){
            //Buscame y muestrame los que coincida con los datos de la tabla
            $query = "SELECT * FROM personas WHERE id LIKE '%".$_POST['query']."%' OR cedula LIKE '%".$_POST['query']."%' OR nombre LIKE '%".$_POST['query']."%' 
            OR genero LIKE '%".$_POST['query']."%' OR placa LIKE '%".$_POST['query']."%' OR ciudad LIKE '%".$_POST['query']."%'" ;
          } else {
            //muestrame todos los datos de la tabla
            $query = "SELECT * FROM personas";
          }
          $resultado = $miconexion->query($query);
          //numero de filas de la consulta en la busqueda
          $contadorF = mysqli_num_rows($resultado);
          //Si no existe un resultado en la busqueda dime que no hay resultados
          if ($contadorF==0) {
            echo "<h3 class='text-center'>No existen registros para la consulta.</h3>";
          } 
          
          
          //Recorre todos los datos que estan mi base de datos  como un array asociativo
          while ($datos = $resultado->fetch_assoc()) {
          ?>          
   
  <div class="card">
  <img  width=200 height=200 src="data:image/jpg;base64, <?php echo base64_encode($datos['imagen']); ?>" >
    <div class="card-body">
      <h5 class="card-title"><?php echo $datos['nombre']; ?></h5>
      <h5 class="card-text"><?php echo $datos['edad'] . " años";?></h5>
      <h5 class="card-text"><?php echo $datos['tipo_persona']; ?></h5>
      
      <?php if ( $datos['genero']=="Masculino"){
         echo "<h5 style='color: green;' class='card-text'>";
         echo  $datos['genero'];
         echo "</h5>";
      }else{
        echo "<h5 style='color: HotPink;' class='card-text'>";
        echo  $datos['genero'];
        echo "</h5>";
      }    
      ?>
      
      <img width=50 height=50 src="https://cdn-icons-png.flaticon.com/512/290/290163.png" alt=""><h5 class="card-text"><?php echo $datos['placa']; ?></h5>
      <!-- <h5 class="card-text" style="color: red"> <?php echo $datos['tipo_vehiculo']; ?></h5> -->
      
      <?php if ( $datos['tipo_vehiculo']=="Carro"){
         echo "<h5><img width=50 height=50 src='https://cdn-icons-png.flaticon.com/512/4770/4770326.png'";
         echo "<br>";
         echo "<h5>";
         echo  $datos['tipo_vehiculo'];
         echo "</h5>";
      }else{
        echo "<h5><img width=50 height=50 src='https://cdn-icons-png.flaticon.com/512/62/62620.png'";
        echo "<br>";
         echo "<h5>";
         echo  $datos['tipo_vehiculo'];
         echo "</h5>";
         
      }    
      ?>

  
    </div>
</div>

  <?php  
            }
            ?>
  
 

  <style type="text/css">
   .imagenindex {
     display: none;
   }
    td, th{
     border: solid 3px;
     text-align: center;
    
   }
   

    
    /* copyring moises-canaria
copyring moises-canaria
copyring moises-canaria
copyring moises-canaria  */
  
  
   </style>

