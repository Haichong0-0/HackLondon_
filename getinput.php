

<!DOCTYPE html>
    <html>
<body>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve the message from the form
    $message = $_POST["user-input"];
    $pack = json_encode($message);
    
    $command = 'python3 test.py';
    $escaped_input_json = escapeshellarg($pack);
    echo $escaped_input_json;

    $output_json = shell_exec("$command $escaped_input_json");
    echo 1;
    echo $output_json;

    // Process the data (you can perform any desired operations here)
    
    // For demonstration purposes, let's simply display the message
} else {
    // If the form is not submitted, redirect to the form page
    header("Location: /index.html");
    exit();
}
?>

</body>
