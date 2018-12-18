<?php

if (!empty($_POST))
{
    $contents = $_POST['contents'];
    echo "POST DATA IS:";
    echo $contents;
}
else // $_POST is empty.
{
    echo "Perform code for page without POST data. ";
}
?>