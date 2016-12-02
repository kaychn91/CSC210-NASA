<?php
$vote = $_REQUEST['vote'];

//get textfile content
$filename = "poll_results.txt";
$content = file($filename);

//putting the content in an array
$array = explode("|", $content[0]);

$action = $array[0];
$act_adv = $array[1];
$adv = $array[2];
$role_play = $array[3];
$sim = $array[4];
$strategy = $array[5];
$sports = $array[6];
$other = $array[7];

if ($vote == 0) {
	$action = $action + 1;
} elseif ($vote == 1) {
	$act_adv = $act_adv + 1;
} elseif ($vote == 2) {
	$adv = $adv + 1;
} elseif ($vote == 3) {
	$role_play = $role_play + 1;
} elseif ($vote == 4) {
	$sim = $sim + 1;
} elseif ($vote == 5) {
	$strategy = $strategy + 1;
} elseif ($vote == 6) {
	$sports = $sports + 1;
} elseif ($vote == 7) {
	$other = $other + 1;
} else {
	
}

//inserts the votes to the txt file
$insertvote = $action."|".$act_adv."|".$adv."|".$role_play."|".$sim."|".$strategy."|".$sports."|".$other;
$fp = fopen($filename, "w"); //don't need file location if poll_results.txt is in the same folder
fputs($fp,$insertvote);
fclose($fp);
?>

<h2>Favorite Game Genre Results:</h2>
<table>
	<tr>
		<td>Action:</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($action/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
				height='20'>
			<?php echo(100*round($action/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Action Adventure:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($act_adv/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($act_adv/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Adventure:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($adv/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($adv/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Role Playing:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($role_play/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($role_play/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Simulator:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($sim/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($sim/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Strategy:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($strategy/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($strategy/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Sports:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($sports/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($sports/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Other:</td>
		<td>
			<img src="images/poll.gif"
			width='<?php echo(100*round($other/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>'
			height='20'>
			<?php echo(100*round($other/($action+$act_adv+$adv+$role_play+$sim+$strategy+$sports+$other),2)); ?>%
		</td>
	</tr>
</table>
