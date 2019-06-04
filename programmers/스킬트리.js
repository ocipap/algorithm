
const solution = (skill, skill_trees) => skill_trees
    .map(x => x.replace(new RegExp(`[^${skill}]`, 'g'), ""))
    .filter(x => skill.indexOf(x) == 0 ||  x === "")
    .length