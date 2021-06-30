echo "Building"
rm ../backend/dist -rf
npm run build
cp dist ../backend/ -r
rm dist -rf
