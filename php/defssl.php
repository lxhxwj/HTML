<?php
ini_set('display_errors', 'On');
//���մ������Ĳ���
//python�ű�Ŀ¼
$script = dirname(dirname(__FILE__)) . '/py/defssl.py';
$output = array();
//$filename = $_FILES['file']['name'];
//$filepath = dirname(__FILE__).'/upload/'.$filename;
//file_put_contents($filepath, file_get_contents($_FILES['file']['tmp_name']));
$cmd    = sprintf('python "%s"', $script);
exec($cmd, $output);
//���python���ص�����
echo '<pre>';
var_dump($output);
?>
