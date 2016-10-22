<html>
<head>
</head>

<body>
  <?php echo '<p> Hello World</p>';

  //php connect to mysql
  $link = mssql_connect('users','monitor', 'MichaelChung1!');

  if(!$link){
    die('Something went wrong while connecting to MSSQL');
  } else {

    echo "hello";
    $version = mssql_query('SELECT * FROM usersdat');
    $row = mssql_fetch_array($version);
    echo $row;
  }



  ?>
</body>

</html>
