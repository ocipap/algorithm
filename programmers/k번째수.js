const f = (arr, [i, j, k]) => arr.slice(i-1, j).sort((a, b) => a-b)[k-1]

const solution = (array, commands) => commands.map(cmd => f(array, cmd))