<?php
ini_set('display_errors', 'On');
//接收传过来的参数
//python脚本目录
$script = dirname(dirname(__FILE__)) . '/py/defssl.py';
$output = array();
//$filename = $_FILES['file']['name'];
//$filepath = dirname(__FILE__).'/upload/'.$filename;
//file_put_contents($filepath, file_get_contents($_FILES['file']['tmp_name']));
$cmd    = sprintf('python "%s"', $script);
exec($cmd, $output);
//输出python返回的数据
echo '<pre>';
var_dump($output);
?>
