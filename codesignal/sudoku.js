function sudoku2(grid) {
    return horizon(grid) && vertical(grid) && area(grid)
}

function horizon(grid) {
    let res = true
    for(let i = 0; i < 9; i++) {
        if(!isSudoku(grid[i])) res = false
    }
    return res
}

function vertical(grid) {
    let res = true
    for(let i = 0; i < 9; i++) {
        let tmp = []
        for(let j = 0; j < 9; j++) {
            tmp.push(grid[j][i])
        }
        if(!isSudoku(tmp)) res = false
    }
    return res
}

function area(grid) {
    let res = true
    let tmp = {
        0 : grid.slice(0, 3),
        1 : grid.slice(3, 6),
        2 : grid.slice(6)
    }
    for(const a in tmp) {
        let lines = {0 : [], 1 : [], 2 : []}
        tmp[a].forEach((el) => {
            el.forEach((element, i) => {
                switch (i) {
                    case 0:
                    case 1:
                    case 2:
                        lines[0].push(element)
                        break;
                    case 3:
                    case 4:
                    case 5:
                        lines[1].push(element)
                        break;
                    case 6:
                    case 7:
                    case 8:
                        lines[2].push(element)
                        break;
                    default:
                        break;
                }
            })
        })
        for(const b in lines) {
            if(!isSudoku(lines[b])) res = false
        }
    }

    return res
}

function isSudoku(line) {
    let res = true
    for(let i = 1; i <= 9 ; i++) {
        let count = 0;
        for(let j = 0; j < 9; j++) {
            if(line[j] == i) count++
            if(count == 2) res = false
        }
    }
    return res
}

console.log(sudoku2([['.', '.', '.', '.', '2', '.', '.', '9', '.'],
['.', '.', '.', '.', '6', '.', '.', '.', '.'],
['7', '1', '.', '.', '7', '5', '.', '.', '.'],
['.', '7', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '8', '3', '.', '.', '.'],
['.', '.', '8', '.', '.', '7', '.', '6', '.'],
['.', '.', '.', '.', '.', '2', '.', '.', '.'],
['.', '1', '.', '2', '.', '.', '.', '.', '.'],
['.', '2', '.', '.', '3', '.', '.', '.', '.']]))