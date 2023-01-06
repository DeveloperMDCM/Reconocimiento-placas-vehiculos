


<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Sistema</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
    <div class="dropdown" >
        <button class="btn btn-info dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true"> Registrar <span class="caret"></span>
        </button>
        <ul class=" dropdown-menu scrollable-menu bg-info" aria-labelledby="dropdownMenu1" style="text-align: center;" >
            <li ><a  style="text-decoration: none; color: #000" href="index.php?page=form">Administrador</a></li>
            <li><a style="text-decoration: none; color: #000;" href="index.php?page=r_conductores">Conductores</a></li>
        </ul>
    </div>
    <a class="nav-link " href="index.php?page=admins">Admins <span class="sr-only">(current)</span></a>
    <a class="nav-link" href="index.php?page=conductores">Conductores <span class="sr-only">(current)</span></a>
    
    </div>
  </div>
  <h4 style="padding: 0 15px ; font-size: 20px">

    <?php 
    //variable que guarda el nombre del login
      echo $_SESSION["auth"] ;
      ?>  
      <div> 
    </h4>
    <!-- cierrame la sesion  -->
    <a  class="btn w-20 btn-danger " href="login/logout.php">Salir</a>
  </div>
</nav>