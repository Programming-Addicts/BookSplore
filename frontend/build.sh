echo "Building"
npm run build
rm ../backend/dist -rf
cp dist ../backend/ -r
rm dist -rf
