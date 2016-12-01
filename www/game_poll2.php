<?php
$vote = $_REQUEST['vote'];

//get textfile content
$filename = "poll2_results.txt";
$content = file($filename);

//putting the content in an array
$array = explode("|", $content[0]);

$game0 = $array[0];
$game1 = $array[1];
$game2 = $array[2];
$game3 = $array[3];
$game4 = $array[4];
$game5 = $array[5];
$game6 = $array[6];
$game7 = $array[7];
$game8 = $array[8];
$game9 = $array[9];

if ($vote == 0) {
	$game0 = $game0 + 1;
} elseif ($vote == 1) {
	$game1 = $game1 + 1;
} elseif ($vote == 2) {
	$game2 = $game2 + 1;
} elseif ($vote == 3) {
	$game3 = $game3 + 1;
} elseif ($vote == 4) {
	$game4 = $game4 + 1;
} elseif ($vote == 5) {
	$game5 = $game5 + 1;
} elseif ($vote == 6) {
	$game6 = $game6 + 1;
} elseif ($vote == 7) {
	$game7 = $game7 + 1;
} elseif ($vote == 8) {
	$game8 = $game8 + 1;
} elseif ($vote == 9) {
	$game9 = $game9 + 1;
} else {
	
}

//inserts the votes to the txt file
$insertvote = $game0."|".$game1."|".$game2."|".$game3."|".$game4."|".$game5."|".$game6."|".$game7."|".$game8."|".$game9;
$fp = fopen($filename, "w"); //don't need file location if poll_results.txt is in the same folder
fputs($fp,$insertvote);
fclose($fp);
?>

<h2>Most Anticipated Games:</h2>
<table>
	<tr>
		<td>Pokémon Sun/Moon</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game0/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game0/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Assassin's Creed:<br>The Ezio Collection</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game1/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game1/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Watch_Dogs 2</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game2/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game2/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Dead Rising 4</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game3/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game3/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>The Last Guardian</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game4/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game4/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Darksiders: Warmastered Edition</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game5/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game5/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Final Fantasy XV</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game6/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game6/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Steins;Gate 0</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game7/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game7/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Steep</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game8/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game8/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
	<tr>
		<td>Super Mario Maker</td>
		<td>
			<img src="images/poll.gif"
				width='<?php echo(100*round($game9/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>'
				height='20'>
			<?php echo(100*round($game9/($game0+$game1+$game2+$game3+$game4+$game5+$game6+$game7+$game8+$game9),2)); ?>%
		</td>
	</tr>
</table>
