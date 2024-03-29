<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset='utf-8' />
    
    <link href='./ics-viewer/fullcalendar.min.css' rel='stylesheet' />
    <link href='./ics-viewer/fullcalendar.print.min.css' rel='stylesheet' media='print' />
    <script src='./ics-viewer/lib/moment.min.js'></script>
    <script src='./ics-viewer/lib/jquery.min.js'></script>
    <script src='./ics-viewer/fullcalendar.min.js'></script>
    <script src='./ics-viewer/ical.min.js'></script>
    <script src='./ics-viewer/urlhash.js'></script>
    <script src='./script.js'></script>
    <title>Main page</title>
    <meta property="og:title" content="main page" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta charset="utf-8" />
    <meta property="twitter:card" content="summary_large_image" />

    <style data-tag="reset-style-sheet">
      html {  line-height: 1.15;}body {  margin: 0;}* {  box-sizing: border-box;  border-width: 0;  border-style: solid;}p,li,ul,pre,div,h1,h2,h3,h4,h5,h6,figure,blockquote,figcaption {  margin: 0;  padding: 0;}button {  background-color: transparent;}button,input,optgroup,select,textarea {  font-family: inherit;  font-size: 100%;  line-height: 1.15;  margin: 0;}button,select {  text-transform: none;}button,[type="button"],[type="reset"],[type="submit"] {  -webkit-appearance: button;}button::-moz-focus-inner,[type="button"]::-moz-focus-inner,[type="reset"]::-moz-focus-inner,[type="submit"]::-moz-focus-inner {  border-style: none;  padding: 0;}button:-moz-focus,[type="button"]:-moz-focus,[type="reset"]:-moz-focus,[type="submit"]:-moz-focus {  outline: 1px dotted ButtonText;}a {  color: inherit;  text-decoration: inherit;}input {  padding: 2px 4px;}img {  display: block;}html { scroll-behavior: smooth  }
    </style>
    <style data-tag="default-style-sheet">
      html {
        font-family: Inter;
        font-size: 16px;
      }

      body {
        font-weight: 400;
        font-style:normal;
        text-decoration: none;
        text-transform: none;
        letter-spacing: normal;
        line-height: 1.15;
        color: var(--dl-color-gray-black);
        background-color: var(--dl-color-gray-white);

      }
    </style>
    <link
      rel="stylesheet"
      href="https://unpkg.com/animate.css@4.1.1/animate.css"
    />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
      data-tag="font"
    />
    <link
      rel="stylesheet"
      href="https://unpkg.com/@teleporthq/teleport-custom-scripts/dist/style.css"
    />
  </head>
  <body>
    <?php
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
      // Retrieve the message from the form
      $message = $_POST["user-input"];
    

    
      $python_script_path = 'test.py';

      //$command = escapeshellcmd("python " . $python_script_path . " " . escapeshellarg($message));
      $command = escapeshellcmd("py " . $python_script_path);

    
      $output = shell_exec($command);


    

      // Process the data (you can perform any desired operations here)
    
      // For demonstration purposes, let's simply display the message
      }   
    ?>
    <link rel="stylesheet" href="./style.css" />
    <div>
      <link href="./index.css" rel="stylesheet" />

      <div class="home-container">
        <div class="home-container1">
          <div class="home-container2">
            <div class="home-container3">
              <span class="home-text">
                <span>Project</span>
                <br />
              </span>
              <span class="home-des">This project is about</span>
            </div>
            <div class="home-container4">
              <form action = "" method="post" id="user-form">          
              <input textarea
                  type="text"
                  placeholder="What Are You Going To Do Next Week?"
                  class="home-textarea textarea"
                  name = "user-input"
                  id= "user-input"
                ></textarea>
                <button type="submit" class="home-button button" id="fetch" onclick="submitForm()">UPDATE</button>
              </form>
              <button type="button" class="home-button1 button">
                IMPORT TO CALENDER
              </button>
            </div>
          </div>
          <div class="home-container5">
            <div id='calendar' ></div>
        
            
          </div>
        </div>
      </div>
    </div>

    <script>
      function submitForm() {
        var formData = new FormData(document.getElementById("user-"));

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "getinput.php", true);

        xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Update the result div with the response from the PHP file
            document.getElementById("result").innerHTML = xhr.responseText;
        }
    };

    xhr.send(formData);
}
    </script>
  </body>
</html>
