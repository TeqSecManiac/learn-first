function minDepth(root){
    if(!root) return 0;
    let depth = 1;
    if(!root.left && !root.right) return depth;
    let queue = [root];
    
    while(queue.length>0){
        let len = queue.length;
        for(let i = 0; i < len; i++){
            root = queue.shift();
            if(!root.left&&!root.right) return depth;
            else{
                // root.left ? queue.push(root.left) : null;
                // root.right? queue.push(root.right): null;
                if(root.left) queue.push(root.left);
                if(root.right) queue.push(root.right)
            }
        }
        depth++;
    }
    return depth;
}
