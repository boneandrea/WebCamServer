find etc -type f -exec echo "==== {} ====" \; -exec diff {} /{} \;
