$data = Get-Content -Path (join-path $PSScriptRoot 'data.txt')

$data | ForEach-Object { $index1 = 0 } {
  [int]$i = [int]$_
  $data | ForEach-Object { $index2 = 0 } {
    if ($index1 -ne $index2 -and [int]$_ + [int]$i -eq 2020) {
      $res = [int]$_ * [int]$i
      Write-Output "$_ + $i == 2020`n$_ * $i == $res"
      break
    }
    $index2++
  }
  $index1++
}
