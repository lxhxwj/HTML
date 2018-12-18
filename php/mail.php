<?php
//ini_set('display_errors', 'On');
$script = dirname(dirname(__FILE__)) . '/py/mail.py';
$output = array();
exec(sprintf('python "%s"', $script), $output);
echo '<pre>';
var_dump($output);die;
//exec('python /var/www/html/mail.py',$outPut);
//print_r($outPut);
?>
